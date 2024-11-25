from sentence_transformers import SentenceTransformer
from nltk.tokenize import sent_tokenize
import numpy as np

class TextAnalyzer:
    def __init__(self):
        print("Loading model...")
        self.model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')
        self.similarity_threshold = 0.80

    def calculate_similarity(self, vec1, vec2):
        # Normalize vectors and calculate cosine similarity
        vec1_normalized = vec1 / np.linalg.norm(vec1)
        vec2_normalized = vec2 / np.linalg.norm(vec2)
        return float(np.dot(vec1_normalized, vec2_normalized))

    def find_redundancies(self, text: str):
        # Debug print
        print("Processing text...")
        
        # Split text into sections
        sections = {}
        current_section = None
        current_points = []

        for line in text.split('\n'):
            line = line.strip()
            if not line:
                continue
            
            # print(f"Processing line: {line[:50]}...")

            if line.endswith(':'):
                if current_section and current_points:
                    sections[current_section] = current_points
                current_section = line[:-1]
                current_points = []
            elif line.startswith('-') and current_section:
                current_points.append(line[1:].strip())

        # Add last section
        if current_section and current_points:
            sections[current_section] = current_points

        # print(f"\nFound {len(sections)} sections")
        #for section, points in sections.items():
        #    print(f"Section '{section}': {len(points)} points")

        redundant_groups = []

        # Process each section
        for section, points in sections.items():
            if len(points) < 2:
                continue

            # Get embeddings for all points in the section
            embeddings = self.model.encode(points)

            # Find similar points
            for i in range(len(points)):
                similar_points = []
                for j in range(len(points)):
                    if i != j:
                        similarity = self.calculate_similarity(
                            embeddings[i],
                            embeddings[j]
                        )
                        # print(f"Comparing points {i} and {j}: similarity = {similarity:.3f}")
                        
                        if similarity > self.similarity_threshold:
                            similar_points.append({
                                'text': points[j],
                                'similarity': round(similarity, 3)
                            })

                if similar_points:
                    redundant_groups.append({
                        'section': section,
                        'main_point': points[i],
                        'similar_points': similar_points
                    })

        return redundant_groups