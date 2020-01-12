# Robo Gong

## Getting Started

```bash
cd ~/
git clone git@github.com:daugihao/robo-gong.git
cd robo-gong
make install
```

> Modify services to watch in `robo_gong/app.py`


## Restart

```bash
sudo supervisorctl restart robo-gong 
```

## Tests

```bash
pip install -r requirements.txt
pip install -r test_requirements.txt
PYTHONPATH=. pytest
```