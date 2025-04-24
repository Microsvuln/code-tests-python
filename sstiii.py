from jinja2 import Template

class TemplateRenderer:
    def __init__(self):
        # Jinja2 doesn't need a configuration object like FreeMarker, just create a Template instance directly
        pass

    def render_template(self, template_content, data):
        template = Template(template_content)
        return template.render(data)


def main():
    renderer = TemplateRenderer()
    input_data = {
        "username": "JohnDoe"
    }

    user_template = "Hello, {{ username }}! Today is {{ 'freemarker.template.utility.Execute' | new() }}"

    try:
        result = renderer.render_template(user_template, input_data)
        print(result)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
