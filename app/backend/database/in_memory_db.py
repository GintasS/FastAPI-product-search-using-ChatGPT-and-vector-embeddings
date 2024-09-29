from database.data_helpers import *
from core.constants import File
import numpy as np

products_embeddings = read_csv(File.PRODUCT_EMBEDDINGS_FILE_PATH)
products_embeddings['Embedding'] = products_embeddings.Embedding.apply(eval).apply(np.array)