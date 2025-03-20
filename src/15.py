class SimpleMathCalculator {
  def calculate(a: float, b: float) -> float:
    return a + b

class CalculatorApp extends React.Component {
  render() {
    return (
      <div>
        <h1>Simple Math Calculator</h1>
        <div>
          <p>A simple mathematics calculator built with React and TypeScript.</p>
          <p>This app allows you to perform various mathematical operations, including addition, subtraction, multiplication, and division. Feel free to use it for your projects or simply play around!</p>
          <div className="calculator">
            <input type="number" value="0" onChange={(e) => setValue(e.target.value)} />
            <button onClick={() => operation('add')}>+</button>
            <button onClick={() => operation('subtract')}>-</button>
            <button onClick={() => operation('multiply')}>x</button>
            <button onClick={() => operation('divide')}>÷</button>
          </div>
        </div>
      </div>
    );
  }

  operation(operation: string) {
    const a = parseFloat(this.state.value);
    const b = parseFloat(this.props.match.params.b);

    if (operation === 'add') {
      this.setState({ result: a + b });
    } else if (operation === 'subtract') {
      this.setState({ result: a - b });
    } else if (operation === 'multiply') {
      this.setState({ result: a * b });
    } else if (operation === 'divide') {
      this.setState({ result: a / b });
    }
  }

  setValue(value: string) {
    const newVal = parseFloat(value);
    this.setState({ value: newVal });
  }
}
