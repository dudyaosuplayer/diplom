import React, { useState } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { createPortal } from 'react-dom';

import Navigation from './components/navigation/Navigation';
import Header from './components/header/Header';
import Footer from './components/footer/Footer';
import Home from './pages/home/Home';
import Projects from './pages/projects/Projects';
import Analitics from './pages/analitics/Analitics';
import Tasks from './pages/tasks/Tasks';
import Agile from './pages/agile/Agile';
import Enter from './pages/enter/Enter';

import './styles/index.scss';

function App() {
  const [isEnered, setIsEnered] = useState( sessionStorage.getItem('user') === null);

  return (
    <div className="App">
      <BrowserRouter>
      <div className='App__left'>
        <Navigation />
      </div>
      <div className='App__center'>
        <Header />
        <Routes>
          <Route path='/' element={<Home /> } />
          <Route path='/projects' element={<Projects /> } />
          <Route path='/tasks' element={<Tasks /> } />
          <Route path='/analitics' element={<Analitics /> } />
          <Route path='/agile' element={ <Agile /> } />
        </Routes>
        <Footer />
      </div>
      
      {isEnered && createPortal(<Enter handleClick={setIsEnered} />, document.body)}      
      </BrowserRouter>
    </div>
    
  );
}

export default App;
