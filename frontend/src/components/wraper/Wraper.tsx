import React from "react";


interface Props {
    classes: string,
    children: React.ReactNode,
}

const Wraper: React.FC<Props> = ({classes, children}) => {
    return (
        <section className={classes}>
            <div className="container">
                {children}
            </div>
        </section>        
    )
}

export default Wraper;