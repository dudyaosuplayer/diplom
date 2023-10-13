import React from "react";
import { Link, useLocation } from "react-router-dom";
import clsx from 'clsx';

import './navigation.scss';

import logo from '../../icons/logo.png';
import home from '../../icons/home.svg';
import document from '../../icons/document.svg';
import folders from '../../icons/folders.svg';
import pictures from '../../icons/pictures.svg';
import task from '../../icons/task-list.svg';

const Navigation: React.FC = () => {
    let location = useLocation();

    let classesHome = clsx('navigation__item',
                    { 'navigation__active': location.pathname === '/' });
    let classesP = clsx('navigation__item',
                    { 'navigation__active': location.pathname === '/projects' });
    let classesT = clsx('navigation__item',
                    { 'navigation__active': location.pathname === '/tasks' });
    let classesA = clsx('navigation__item',
                    { 'navigation__active': location.pathname === '/analitics' });   
    let classesAg = clsx('navigation__item',
                    { 'navigation__active': location.pathname === '/agile' });

    return (
        <div className="navigation">
            <div className="logo">
                <Link to="/" className="logo">
                    <img src={logo} alt="" />
                </Link>
            </div>
              
            <nav className="nav">
                <Link to="/" >
                    <div className={classesHome}>
                        <img src={home} alt="" />
                        <p>Главная</p>
                    </div>    
                </Link>

                <Link to="/projects" >
                    <div className={classesP}>
                        <img src={document} alt="" />
                        <p>Проекты</p>
                    </div>    
                </Link>

                <Link to="/tasks" >
                    <div className={classesT}>
                        <img src={task} alt="" />
                        <p>Задачи</p>
                    </div>    
                </Link>

                <Link to="/analitics" >
                    <div className={classesA}>
                        <img src={folders} alt="" />
                        <p>Отчеты</p>
                    </div>    
                </Link>

                <Link to="/agile" >
                    <div className={classesAg}>
                        <img src={pictures} alt="" />
                        <p>Доска Agile</p>
                    </div>    
                </Link>
            </nav>
        </div>
    )
}

export default Navigation;