from src import cli, solar_panels
from src.utils.counter import recursive_list_count


def main():
    action = None

    while action != 'quit':
        tier = cli.choose_from('tier', *map(str, range(1, 7)))

        amount = ''
        while not amount.isdigit():
            amount = cli.ask('Choose an amount [1]') or '1'

        amount = int(amount)

        to_craft = solar_panels[int(tier) - 1].get_raw_recipe() * amount
        count = recursive_list_count(to_craft)

        cli.pretty_list(
            "Total ressources needed",
            (f"{k} x{v:,}" for k, v in sorted(count.items()))
        )

        action = cli.choose_from('action', 'get materials', 'quit')


if __name__ == '__main__':
    main()
