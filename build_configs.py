from jinja2 import Environment, FileSystemLoader
import os


# Add the folder where templates are when creating the BuildConfig object.
# Pass in the filename path you want to save after the template is build
# Pass in the variables you want to be passed into the template
# Pass in the template you want to use
class BuildConfigs():
    def __init__(self, template_folder):
        PATH = os.path.dirname(os.path.abspath(__file__))
        self.TEMPLATE_ENVIRONMENT = Environment(
            autoescape=False,
            loader=FileSystemLoader(os.path.join(PATH, template_folder)),
            trim_blocks=False)

    def render_template(self, template_filename, template_variables):
        return self.TEMPLATE_ENVIRONMENT.get_template(template_filename). \
               render(template_variables)

    def build_config(self, output_filename, template_variables,
                     template_filename):
        # fname = output_filename
        with open(output_filename, 'w') as f:
            jinja_render = self.render_template(template_filename,
                                                template_variables)
            f.write(jinja_render)
