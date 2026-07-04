from src.shared.preferences import UserPreferences


class AgentSelector:
    """
    Chooses the best candidate according to user preferences.
    """

    def select(self, candidates, preferences: UserPreferences):

        if not candidates:
            return None

        filtered = []

        for agent in candidates:

            if agent.score < preferences.minimum_score:
                continue

            if preferences.prefer_free and agent.cost != "Free":
                continue

            if preferences.prefer_local and agent.source == "Local":
                filtered.insert(0, agent)
            else:
                filtered.append(agent)

        if not filtered:
            filtered = candidates

        filtered.sort(key=lambda a: a.score, reverse=True)

        return filtered[0]