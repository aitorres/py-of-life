# Py of Life

Python implementation of Conway's Game of Life using no dependency other than Python's standard library.

Tested against Python 3.9, 3.10 and 3.11.

## Installation

No need to install anything else! If you've got Python 3.9+ on your system, then just clone the repo
(or copy the content of [py_of_life.py]([./py_of_life.py]) over to a local file).

## Usage

```bash
python py_of_life.py <HEIGHT> <WIDTH> <ITERS>
```

The program needs three values to run, all of them integers greater than 0:

- A height `N` an a width `M` in order to create an `NxM` grid
- An amount of iterations / generations (4 generations will run per second)

For example:

```bash
python py_of_life.py 10 25 50
```

You also run `python py_of_life.py --help` to get these instructions printed to your CLI.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

Licensed under the [GNU Affero General Public License](./LICENSE).
