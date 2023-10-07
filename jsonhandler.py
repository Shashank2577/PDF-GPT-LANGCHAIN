from langchain.document_loaders import JSONLoader

data = JSONLoader(file_path="test_translated.json",jq_schema='mediawiki.page[].title')
print(data)

