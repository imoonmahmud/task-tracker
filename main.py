import click

# @click.command()
# @click.option('--name', default='World', help='Who to greet.')
# @click.option('--count', default=1, help='Number of greetings')
# def hello(name, count):
#     for _ in range(count):
#         click.echo(f'Hello, {name}')

@click.command()
@click.option('a', type=int)
@click.option('b')
def sum(a, b):
    print(a + b)

if __name__ == '__main__':
    sum()