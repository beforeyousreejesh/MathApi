import os
import unittest

from main import create_app
from __init_ import blueprint

app = create_app(os.getenv("ENV_B_NAME") or "dev")
app.register_blueprint(blueprint)

@app.cli.command("run")
def run():
    app.run()

@app.cli.command("test")
def test():
    """Runs the unit tests."""
    tests=unittest.TestLoader().discover('test',pattern='test*.py')
    result=unittest.TextTestRunner(verbosity=2).run(tests)
    if(result.wasSuccessful()):
        return 0
    return 1

if(__name__=="__main__"):
    app.cli()