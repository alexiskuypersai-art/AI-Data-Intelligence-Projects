"""
Module: NLP Pipeline Data Navigator
Description: A collection of utility functions to navigate, calculate, 
             and repair nested JSON structures from AI processing pipelines.
Author: [Ton Nom/Pseudo]
"""

def find_entity_value(raw_data, target_doc_id, target_step_name, entity_label):
    """
    Finds a specific entity value by its label within a deeply nested document structure.
    
    Args:
        raw_data (list): The list of document dictionaries.
        target_doc_id (str): ID of the document to search.
        target_step_name (str): The pipeline step (e.g., 'NER').
        entity_label (str): The label to find (e.g., 'ORG').
        
    Returns:
        str: The value of the entity if found, None otherwise.
    """
    for document in raw_data:
        if document["doc_id"] == target_doc_id:
            for pipeline_step in document["steps"]:
                if pipeline_step["name"] == target_step_name:
                    # Navigation into entities list: [label, value, position]
                    for entity in pipeline_step['entities']:
                        if entity[0] == entity_label:
                            return entity[1]
    return None


def calculate_ocr_confidence_mean(raw_data, target_doc_id):
    """
    Calculates the average confidence score for OCR results in a specific document.
    
    Args:
        raw_data (list): The list of document dictionaries.
        target_doc_id (str): ID of the document to analyze.
        
    Returns:
        float: The calculated mean confidence, rounded to 2 decimal places.
    """
    total_confidence = 0
    result_count = 0
    
    for document in raw_data:
        if document["doc_id"] == target_doc_id:
            for pipeline_step in document['steps']:
                if pipeline_step["name"] == "OCR":
                    for result in pipeline_step['results']:
                        total_confidence += result["conf"]
                        result_count += 1
    
    if result_count == 0:
        return 0.0
        
    return round(total_confidence / result_count, 2)


def inject_missing_step(raw_data, target_doc_id, new_step_data):
    """
    Injects a missing processing step into a specific document's pipeline.
    
    Args:
        raw_data (list): The list of document dictionaries.
        target_doc_id (str): ID of the document to repair.
        new_step_data (dict): The step dictionary to append.
    """
    for document in raw_data:
        if document['doc_id'] == target_doc_id:
            document['steps'].append(new_step_data)
            return True
    return False


# --- EXECUTION EXAMPLE ---
if __name__ == "__main__":
    # Sample data for demonstration
    mock_data = [
        {
            "doc_id": "FACT_99",
            "steps": [
                {"name": "OCR", "results": [{"conf": 0.90}, {"conf": 0.80}]},
                {"name": "NER", "entities": [["ORG", "SpaceX", (0, 6)]]}
            ]
        },
        {
            "doc_id": "FACT_100",
            "steps": []
        }
    ]

    # Testing Mission A
    org_name = find_entity_value(mock_data, "FACT_99", "NER", "ORG")
    print(f"Extraction - Organization: {org_name}")

    # Testing Mission B
    mean_conf = calculate_ocr_confidence_mean(mock_data, "FACT_99")
    print(f"Analysis - OCR Average Confidence: {mean_conf}")

    # Testing Mission C
    repair_step = {"name": "NER", "entities": []}
    if inject_missing_step(mock_data, "FACT_100", repair_step):
        print(f"Repair - Successfully injected NER step into FACT_100")
