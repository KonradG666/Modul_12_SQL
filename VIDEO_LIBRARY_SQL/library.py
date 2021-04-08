from app import app, db
from app.models import Band, Video


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Band": Band, "Video": Video}
