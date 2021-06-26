# dopey - Another Brainf*ck Interpreter

The dopey brainf\*ck interpreter was created as a side project to become familiar with Python 3. The goal was to fully implement all the features of brainf\*ck as defined in this [wiki page](https://en.wikipedia.org/wiki/Brainfuck#Language_design) into dopey.

## Demo
![gif](https://i.imgur.com/9HbBB1k.gif)

## Implemetation Limitations

The dopey is limited to a memory buffer of **30,000** byte cells all initialized to zero. Any attempts to move the pointer past the bounds of the memory buffer will result in an exception being raised. Attempting to print any cell with a value outside of the defined ASCII characters may also result in an exception.

## Requirements

Make sure you've installed Python 3. You can download and install Python 3 at [python.org](https://www.python.org/downloads/).

Verify you have Python 3 installed by running the following:

```bash
python --version
```
or in some systems
```bash
python3 --version
```

## Running dopey

Clone the Github repository and from your terminal move to the root of the project and run the following lines:

```bash
chmod +x dopey.py
./dopey.py my_file.bf
```

You can also import an interpreter class included with dopey and use it in your own python scripts.

```python
from dopey import Interpreter

interpreter = Interpreter()
interpreter.execute("[brainf*ck code]++-->><<++--")
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)