import os

types = {
    "Binary": "Expr left, Token operator, Expr right",
    "Grouping": "Expr expression",
    "Literal": "Object value",
    "Unary": "Token operator, Expr right"
}


def define_ast(filename='Expr.java', output_dir='./', basename='Expr', types=types):
    with open(filename, 'w') as f:
        f.write(f'package org.example;{os.linesep * 2}')
        f.write(f'import java.util.List;{os.linesep}')
        f.write(f'import org.example.Token;{os.linesep * 2}')

        f.write(f'abstract class {basename}' + '{' + os.linesep)
        define_visitor(f, basename, types)

        for key, value in types.items():
            class_name = key
            fields = value
            define_type(f, basename, class_name, fields)

        f.write(os.linesep)
        f.write("  abstract <R> R accept(Visitor<R> visitor);" + os.linesep)
        f.write("}")


def define_visitor(f, basename, types):
    f.write(' interface Visitor<R> {' + os.linesep)
    for x, y in types.items():
        f.write("   R visit" + x + basename + "(" +
                x + " " + basename.lower() + ")" + ";" + os.linesep)
    f.write("  }" + os.linesep)


def define_type(f, basename, class_name, fields):
    f.write(f" static class {class_name} extends {basename} " + "{" + os.linesep)
    f.write(f"     {class_name} ({fields}) " + "{" + os.linesep)

    values = fields.split(", ")
    for value in values:
        name = value.split(" ")[1]
        f.write("     this." + name + "=" + name + ";" + os.linesep)

    f.write("    }" + os.linesep)

    f.write("    @Override" + os.linesep)
    f.write("    <R> R accept(Visitor<R> visitor) {" + os.linesep)
    f.write("     return visitor.visit" + class_name + basename + "(this);" + os.linesep)
    f.write("   }" + os.linesep)

    for value in values:
        f.write("   final " + value + ";" + os.linesep)
    f.write("   }" + os.linesep)


def main():
    define_ast()


if __name__ == '__main__':
    main()
