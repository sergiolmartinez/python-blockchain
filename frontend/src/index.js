import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import history from './history';
import './index.css';
import App from './components/App';
import Blockchain from './components/Blockchain';
import ConductTransaction from './components/ConductTransaction';
import TransactionPool from './components/TransactionPool';

ReactDOM.render(
  <Router history={history}>
    <Routes>
      <Route path='/' element={<App/>}/>
      <Route path='/blockchain' element={<Blockchain/>} />
      <Route path='/conduct-transaction' element={<ConductTransaction/>} />
      <Route path='/transaction-pool' element={<TransactionPool/>} />
    </Routes>
  </Router>,
  document.getElementById('root')
);

