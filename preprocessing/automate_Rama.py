import os
import re
import pandas as pd
from sklearn.preprocessing import LabelEncoder


def clean_text(text: str) -> str:
    """
    Fungsi untuk membersihkan teks, apa saja:
    - lowercase
    - menghapus newline
    - menghapus karakter non-alfabet
    - rapikan spasi
    """
    if pd.isna(text):
        return ""

    text = text.lower()
    text = re.sub(r"\n+", " ", text)
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def preprocess_bbc_news(
    input_path: str,
    output_path: str
) -> pd.DataFrame:
    """
    Fungsi untuk
    Melakukan preprocessing otomatis pada dataset BBC News.
    """

    df = pd.read_csv(input_path, sep=",", engine="python")

    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    if "labels" in df.columns:
        df.rename(columns={"labels": "label"}, inplace=True)

    required_columns = [
        "text",
        "label",
        "no_sentences",
        "flesch_reading_ease_score",
        "dale_chall_readability_score"
    ]

    df = df[required_columns]

    df = df.dropna()

    df = df.drop_duplicates()

    df["clean_text"] = df["text"].apply(clean_text)

    label_encoder = LabelEncoder()
    df["label_encoded"] = label_encoder.fit_transform(df["label"])

    final_df = df[
        [
            "clean_text",
            "label_encoded",
            "no_sentences",
            "flesch_reading_ease_score",
            "dale_chall_readability_score"
        ]
    ]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    final_df.to_csv(output_path, index=False)

    return final_df


if __name__ == "__main__":
    INPUT_DATASET = "../bbc_news_raw/bbc_news.csv"
    OUTPUT_DATASET = "./bbc_news_preprocessing.csv"

    preprocess_bbc_news(
        input_path=INPUT_DATASET,
        output_path=OUTPUT_DATASET
    )

    print("Preprocessing selesai. Dataset tersimpan pada:", OUTPUT_DATASET)
