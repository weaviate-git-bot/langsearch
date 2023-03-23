from langsearch.pipelines.common.index import SimpleIndexPipeline
from langsearch.pipelines.common.storeitem import StoreItemPipeline
from langsearch.pipelines.common.textsplitter import TextSplitterPipeline
from langsearch.pipelines.common.python_readability import PythonReadabilityPipeline
from langsearch.pipelines.common.inscriptis import InscriptisPipeline
from langsearch.pipelines.types.enumerations import ItemType
from langsearch.pipelines.types.text.html import HTMLFromTextPipeline


class GenericTextPipeline:
    """
    Built-in pipelines should always use priorities between 400 and 600.
    """
    ITEM_TYPE = ItemType.TEXT

    ITEM_PIPELINES = {
        HTMLFromTextPipeline: 400,
        PythonReadabilityPipeline: 410,
        InscriptisPipeline: 420,
        TextSplitterPipeline: 430,
        StoreItemPipeline: 440,
        SimpleIndexPipeline: 450
    }

    HTML_FROM_TEXT_PIPELINE_INPUTS = {
        "text": lambda item: getattr(item["response"], "text"),
        "url": lambda item: getattr(item["response"], "url")
    }

    PYTHON_READABILITY_PIPELINE_INPUTS = {
        "html": HTMLFromTextPipeline.HTML,
        "url": lambda item: getattr(item["response"], "url")
    }

    INSCRIPTIS_PIPELINE_INPUTS = {
        "html": PythonReadabilityPipeline.HTML_WITHOUT_BP,
        "url": lambda item: getattr(item["response"], "url")
    }

    TEXT_SPLITTER_PIPELINE_INPUTS = {
        "text": InscriptisPipeline.EXTRACTED_TEXT,
        "url": lambda item: getattr(item["response"], "url")
    }

    STORE_ITEM_PIPELINE_INPUTS = {
        "text": InscriptisPipeline.EXTRACTED_TEXT,
        "url": lambda item: getattr(item["response"], "url")
    }

    SIMPLE_INDEX_PIPELINE_INPUTS = {
        "sections": TextSplitterPipeline.SECTIONS,
        "url": lambda item: getattr(item["response"], "url"),
        "changed": StoreItemPipeline.CHANGED
    }

    PIPELINE_INPUTS = {
        HTMLFromTextPipeline: HTML_FROM_TEXT_PIPELINE_INPUTS,
        PythonReadabilityPipeline: PYTHON_READABILITY_PIPELINE_INPUTS,
        InscriptisPipeline: INSCRIPTIS_PIPELINE_INPUTS,
        TextSplitterPipeline: TEXT_SPLITTER_PIPELINE_INPUTS,
        StoreItemPipeline: STORE_ITEM_PIPELINE_INPUTS,
        SimpleIndexPipeline: SIMPLE_INDEX_PIPELINE_INPUTS
    }
