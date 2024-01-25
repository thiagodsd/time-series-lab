"""
This is a boilerplate pipeline 'data_preparation'
generated using Kedro 0.19.2
"""

from kedro.pipeline import Pipeline, node, pipeline
from kedro.pipeline.modular_pipeline import pipeline
from .nodes import get_history_data

def create_pipeline(**kwargs) -> Pipeline:
    _ = kwargs
    template_history_data = pipeline(
        [
            node(
                func=get_history_data,
                inputs=dict(quote_options="params:quote_options"),
                outputs="history_freq_1d",
                name="get_history_data",
                tags=["data_preparation"],
            )
        ]
    )

    btc_pipeline_pdr = pipeline(
        pipe=template_history_data,
        namespace="btc",
    )

    return btc_pipeline_pdr
