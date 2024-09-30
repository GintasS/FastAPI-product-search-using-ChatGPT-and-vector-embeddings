import numpy as np
import pandas as pd

from api.openai_api_helper import get_embedding

def cosine_similarity(a, b):
  if len(a) > len(b):
      b = np.pad(b, (0, len(a) - len(b)), 'constant')
  elif len(b) > len(a):
      a = np.pad(a, (0, len(b) - len(a)), 'constant')
  return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def get_similarity_dataframe(query: str, dataset: pd.core.frame.DataFrame, rows: int) -> pd.core.frame.DataFrame:
  SIMILARITIES_RESULTS_THRESHOLD = 0.70

  # create a copy of the dataset
  dataset_vectors = dataset.copy()

  # get the embeddings for the query    
  query_embeddings = get_embedding(query)

  # create a new column with the calculated similarity for each row
  dataset_vectors["similarity"] = dataset_vectors["Embedding"].apply(
      lambda x: cosine_similarity(np.array(query_embeddings), np.array(x))
  )

  # filter the videos by similarity
  mask = dataset_vectors["similarity"] >= SIMILARITIES_RESULTS_THRESHOLD
  dataset_vectors = dataset_vectors[mask].copy()

  # sort the videos by similarity
  dataset_vectors = dataset_vectors.sort_values(by="similarity", ascending=False).head(
      rows
  )

  # return the top rows
  return dataset_vectors.head(rows)