# Time Series Lab

## Data Preparation

```sh
kedro run --pipeline=data_preparation -n "btc.get_history_data"
```

## Snippets

```sh
python -m ipykernel install --user --name=env_moderadamente --display-name="time-series-lab"
```

```sh
black src/time_series_lab/pipelines/data_preparation/nodes.py 
black src/time_series_lab/pipelines/data_preparation/pipeline.py 
```