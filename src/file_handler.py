import os


def save_resume(uploaded_file):

    os.makedirs(
        "data/resumes",
        exist_ok=True
    )

    file_path = os.path.join(
        "data/resumes",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path