import pytest

# サンプルデータを準備するフィクスチャー
@pytest.fixture
def sample_data():
    return {"key": "value"}

# フィクスチャーを引数として渡す
def test_sample(sample_data):
    # sample_data はフィクスチャーから提供された辞書データ
    assert sample_data["key"] == "value"

