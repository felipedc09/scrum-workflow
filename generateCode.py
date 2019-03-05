from os import mkdir
from os.path import exists, dirname, join
import jinja2
from scrum import get_scrum_mm


def main(debug=False):

    this_folder = dirname(__file__)

    scrum_mm = get_scrum_mm(debug)

    # Build Person model from person.ent file
    gestion_mm = scrum_mm.model_from_file(join(this_folder, 'example.sr'))

    # Create output folder
    srcgen_folder = join(this_folder, 'srcgen')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)


    # Load template
    template = jinja_env.get_template('scrum.template')

    for project in gestion_mm.projects:
        # For each entity generate html file
        with open(join(srcgen_folder,
                       "project%s.html" % project.name.capitalize()), 'w') as f:
            f.write(template.render(project=project))

if __name__ == "__main__":
    main()