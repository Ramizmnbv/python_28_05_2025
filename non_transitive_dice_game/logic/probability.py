class ProbabilityCalculator:
    @staticmethod
    def calculate(user_faces, comp_faces):
        wins = 0
        total = 0
        for u in user_faces:
            for c in comp_faces:
                if u > c:
                    wins += 1
                total += 1
        return wins / total if total > 0 else 0