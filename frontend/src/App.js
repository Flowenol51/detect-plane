
import './App.css';
import axios from 'axios';
function App() {

    console.log(axios.get('http://localhost:5000/'));
    return <p>Hello world</p>
  }

export default App;
