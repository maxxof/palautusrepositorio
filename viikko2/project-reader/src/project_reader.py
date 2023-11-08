from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        parsed = toml.loads(content)
        name = parsed["tool"]["poetry"]["name"]
        description = parsed["tool"]["poetry"]["description"]
        dependecies = parsed["tool"]["poetry"]["dependencies"]
        dev_dependencies = parsed["tool"]["poetry"]["group"]["dev"]["dependencies"]
        license = parsed["tool"]["poetry"]["license"]
        authors = parsed["tool"]["poetry"]["authors"]

        return Project(name, description, dependecies, dev_dependencies, license, authors)
