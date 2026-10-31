#!/bin/bash
#SBATCH --job-name=cf_cora_recover500
#SBATCH --output=$WORKSPACE/production_run_2026-07-27/llmgraphcf_cora/cf_recover_max500_%j.log
#SBATCH --account=<ACCOUNT>
#SBATCH --gres=gpu:v100-32g:1
#SBATCH --time=04:00:00
#SBATCH --mem=32G

cd $WORKSPACE/llm-graph-cf
source venv/bin/activate

python src/cf_gnnfeatures.py \
    --cora_data_path $WORKSPACE/cora_canonical.pt \
    --gnn_ckpt pretrained/sage_canonical.pt \
    --node_words_path data/cora_vocab.json \
    --output_dir data/cora/cf-gnnfeatures-canonical-recovered-max500 \
    --split_path $WORKSPACE/LOGIC2/GSPELL/cora_splits_seed42.npz \
    --seed 42 \
    --max_steps 500 \
    --target_node_ids 36,89,90,122,127,146,154,161,200,201,202,206,234,264,268,293,330,335,369,395,399,418,474,499,540,546,550,574,580,600,606,608,623,635,698,703,728,747,753,769,779,823,854,860,863,928,954,971,975,1012,1016,1021,1038,1060,1065,1069,1092,1122,1126,1130,1136,1139,1141,1147,1148,1153,1184,1205,1212,1215,1218,1219,1238,1243,1257,1282,1296,1300,1363,1365,1470,1492,1516,1527,1531,1534,1571,1597,1631,1634,1661,1676,1685,1696,1787,1799,1806,1884,1890,1931,1974,1981,1982,1986,2027,2088,2146,2156,2182,2197,2265,2274,2298,2306,2336,2343,2385,2459,2499,2510,2513,2517,2533,2542,2553,2562,2579,2583,2612,2631,2638,2660,2676
