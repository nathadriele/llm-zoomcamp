from typing import Dict, List

import spacy


@transformer
def lemmatize_text(documents: List[Dict], *args, **kwargs) -> List[Dict]:
    count = len(documents)
    print('Documents', count)

    nlp = spacy.load('en_core_web_sm')

    data = []

    for idx, document in enumerate(documents):
        document_id = document['document_id']
        if idx % 100 == 0:
            print(f'{idx + 1}/{count}')

        # Process the text chunk using spaCy
        chunk = document['chunk']
        doc = nlp(chunk)
        tokens = [token.lemma_ for token in doc]

        data.append(
            dict(
                chunk=chunk,
                document_id=document_id,
                tokens=tokens,
            )
        )

    print('\nData', len(data))

    return [data]
