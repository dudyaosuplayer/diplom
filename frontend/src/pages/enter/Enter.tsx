import React from "react";

import { Formik, Form } from 'formik';
import * as Yup from "yup";
import Button from "../../components/button/Button";
import Input from "../../components/input/Input";

import "../../styles/main.scss";
import "./enter.scss";

const validationSchema = Yup.object().shape({
    login: Yup.string().trim().required("Incorrect email address"),
    password: Yup.string().trim().min(6, "Пароль не может быть меньше 6 символов")
        .max(8, "Пароль не может быть больше 8 символов").required("Введите пароль"),
});


interface Props {
    handleClick: Function,
}

const Enter: React.FC<Props> = (props) => {
    return (
        <div className="enter">
            <div className="enter__container">
                <h1 className="enter__title">Войти в Neoflex Task Manager</h1>

                <Formik
                    initialValues={{ 
                        login: '',
                        password: '',
                    }}
                    validateOnChange={false}
                    validateOnBlur={true}
                    onSubmit={(val) => {
                        console.log('submit');
                        sessionStorage.setItem('user', 'Вася');
                        props.handleClick(false);
                    }}
                    validationSchema={validationSchema}
                >
                    {({values, errors, isSubmitting}) => (
                        <Form className="enter__form" >
                            <Input type='text' name='login' label='Логин' 
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    required={true} 
                                />

                            <div>
                                <Input type='text' name='password' label='Пароль' 
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    required={true} 
                                />

                                <p className="enter__text">От 6 до 8 символов, цифры, заглавные буквы, строчные буквы.</p>
                            </div>
                            
                            <div className="form__buttons">
                                <Button type="submit" text='Войти' />
                            </div> 
                        </Form>
                    )}
                </Formik>  
            </div> 
        </div>
    )
}

export default Enter;