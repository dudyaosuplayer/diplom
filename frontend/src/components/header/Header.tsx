import React from "react";
import { useLocation } from "react-router-dom";

import './header.scss';

const Header: React.FC = () => {
    let location = useLocation();

    let text = ''

    switch(location.pathname) {
        case '/':  
          text='Главная'
          break
      
        case '/projects': 
          text='Проекты'
          break

        case '/tasks':  
          text='Задачи'
          break
      
        case '/analitics': 
          text='Отчеты'
          break

        case '/agile':  
          text='Доска Agile'
          break
    }
    
    return (
        <header>
            <h1>{text}</h1>
        </header>
    )
}

export default Header;