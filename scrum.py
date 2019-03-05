from os.path import join, dirname
from textx import metamodel_from_file
from textx.export import metamodel_export, model_export


def get_scrum_mm(debug=False):
    this_folder = dirname(__file__)
    scrum_mm = metamodel_from_file(
        join(this_folder, 'scrum.tx'), debug=debug)
    return scrum_mm

def main(debug=False):

    this_folder = dirname(__file__)

    # Create metamodel from textX description
    scrum_mm = get_scrum_mm(debug)

    # Export to dot
    # Create png image with: dot -Tpng -O workflow_meta.dot
    metamodel_export(scrum_mm, join(this_folder, 'Models/scrum_meta.dot'))

    # Load example model
    example = scrum_mm.model_from_file(join(this_folder, 'example.sr'))

    # Export to dot
    # Create png image with: dot -Tpng -O example.dot
    model_export(example, join(this_folder, 'Models/example.dot'))


if __name__ == '__main__':
    main()