# Datasets

All data in this repo is **generated**, so nothing here is real or personal.

| Script | Produces | Used by |
|---|---|---|
| `gen_auth_log.py` | Synthetic SSH `auth.log` with brute-force attacks | Watchtower 02, 03 |
| `gen_transactions.py` | Synthetic crypto transactions with a peel chain | Ledger 02 |

```bash
cd labs/datasets
python3 gen_auth_log.py > sample_auth.log
python3 gen_transactions.py > sample_transactions.csv
```
