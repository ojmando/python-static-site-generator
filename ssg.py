import typer

from ssg.site import Site


def main(source="content", dest="dist"):
    config = dict()
    config["source"] = source
    config["dest"] = dest
    my_site = Site(**config)
    my_site.build()


typer.run(main())
