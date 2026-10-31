import torch
import torch.nn.functional as F
from torch_geometric.nn import SAGEConv


class GraphSAGE(torch.nn.Module):
    """
    2-layer GraphSAGE matching the architecture used in LOGIC2/GSPELL and GraphNarrator:
      SAGEConv(in_channels -> hidden_channels) -> ReLU
      SAGEConv(hidden_channels -> hidden_channels) -> ReLU
      Linear(hidden_channels -> out_channels)   [decoder]
    No batch norm, no dropout (dropout=0.0 by default).
    """

    def __init__(
        self,
        in_channels: int = 1433,
        hidden_channels: int = 768,
        out_channels: int = 7,
        num_layers: int = 2,
        dropout: float = 0.0,
    ):
        super().__init__()
        assert num_layers >= 2, "num_layers must be at least 2"
        self.dropout = dropout

        self.convs = torch.nn.ModuleList()
        self.convs.append(SAGEConv(in_channels, hidden_channels))
        for _ in range(num_layers - 1):
            self.convs.append(SAGEConv(hidden_channels, hidden_channels))
        self.decoder = torch.nn.Linear(hidden_channels, out_channels)

    def forward(self, x: torch.Tensor, edge_index: torch.Tensor) -> torch.Tensor:
        for conv in self.convs:
            x = conv(x, edge_index)
            x = F.relu(x)
            if self.dropout > 0.0:
                x = F.dropout(x, p=self.dropout, training=self.training)
        x = self.decoder(x)
        return x

    @torch.no_grad()
    def predict_proba(self, x: torch.Tensor, edge_index: torch.Tensor) -> torch.Tensor:
        """Return softmax probabilities."""
        return F.softmax(self.forward(x, edge_index), dim=-1)

    @torch.no_grad()
    def predict(self, x: torch.Tensor, edge_index: torch.Tensor) -> torch.Tensor:
        """Return predicted class indices."""
        return self.forward(x, edge_index).argmax(dim=-1)
