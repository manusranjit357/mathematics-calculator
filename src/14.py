import { useState } from 'react';

function Calculator() {
  const [value1, setValue1] = useState('');
  const [value2, setValue2] = useState('');
  const [result, setResult] = useState('');

  const handleClick = () => {
    const equation = `${value1} ${operation} ${value2}`;
    try {
      const result = eval(equation);
      setResult(result.toString());
    } catch (error) {
      alert(`Invalid input: ${error.message}`);
    }
  };

  return (
    <div className="calculator">
      <input type="text" value={value1} onChange={e => setValue1(e.target.value)} />
      <input type="text" value={value2} onChange={e => setValue2(e.target.value)} />
      <button onClick={handleClick}>Calculate</button>
      <p>{result}</p>
    </div>
  );
}
