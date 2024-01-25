import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('fivethirtyeight')

import math
from functools import lru_cache, partial
from typing import Iterable, Optional

import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import torch
from accelerate import Accelerator
from evaluate import load
from gluonts.dataset.field_names import FieldName
from gluonts.dataset.loader import as_stacked_batches
from gluonts.dataset.multivariate_grouper import MultivariateGrouper
from gluonts.itertools import Cached, Cyclic
from gluonts.time_feature import (TimeFeature, get_lags_for_frequency,
                                  get_seasonality,
                                  time_features_from_frequency_str)
from gluonts.transform import (AddAgeFeature, AddObservedValuesIndicator,
                               AddTimeFeatures, AsNumpyArray, Chain,
                               ExpectedNumInstanceSampler, InstanceSplitter,
                               RemoveFields, RenameFields, SelectFields,
                               SetField, TestSplitSampler, Transformation,
                               ValidationSplitSampler, VstackFeatures)
from gluonts.transform.sampler import InstanceSampler
from IPython.display import display
from pandas.core.arrays.period import period_array
from torch import nn
from torch.optim import AdamW
from transformers import (InformerConfig, InformerForPrediction,
                          PretrainedConfig)
from transformers.utils import send_example_telemetry
