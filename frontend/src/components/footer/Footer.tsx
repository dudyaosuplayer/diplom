import React from "react";
import { Link } from "react-router-dom";

import logo from '../../icons/logo.png';

import './footer.scss';

const Footer: React.FC = () => {
    return (
        <footer>
            <div className="container">
                <div className="footer__contacts"> 
                    <Link to="/" >
                        <img src={logo} alt="" />
                    </Link>

                    <address>
                        <ul>
                            <li>
                                <a href="mailto:info@neoflex.ru" className="footer__text">
                                    info@neoTaskManager.ru
                                </a>
                            </li>
                            <li>
                                <a href="tel:+74959842513" className="footer__phone">
                                    +7 (999) 888 77 66
                                </a>
                            </li>
                        </ul>
                    </address>
                </div>
            </div>
        </footer>
    )
}

export default Footer;