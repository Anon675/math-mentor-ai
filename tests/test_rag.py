import pytest
from rag.retriever import Retriever


@pytest.fixture
def retriever():
    return Retriever()


def test_rag_retrieval(retriever):

    query = "quadratic formula"

    results = retriever.retrieve(query)

    assert isinstance(results, list)