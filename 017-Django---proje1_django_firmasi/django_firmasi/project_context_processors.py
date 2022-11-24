def global_context(request):
    FAKE_DB_PROJECTS = [
        f"https://picsum.photos/id/{id}/100/80" for id in range(21, 29)
    ]
    return dict(
        FAKE_DB_PROJECTS=FAKE_DB_PROJECTS,
    )