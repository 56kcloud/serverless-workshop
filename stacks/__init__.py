from os import environ


def ressource_id(sufix: str):
    team = environ.get('TEAM', 'main').title()
    return f'{team}{sufix}'
