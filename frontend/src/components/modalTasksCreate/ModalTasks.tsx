import React, { useState } from "react";
import { Formik, Form } from 'formik';
import * as Yup from "yup";

import Button from "../button/Button";
import Input from "../input/Input";
import Select from "../select/Select";

import './modal.scss';


const validationSchema = Yup.object().shape({
    name: Yup.string().required("Put the name"),
    description: Yup.string().required("Put the description"),
    executor: Yup.string().required("Who will do it"),
    status: Yup.string().required("Select one of the options"),
    priority: Yup.string().required("Select one of the options"),
});

interface Props {
    handleClick: Function
}

const ModalTasks: React.FC<Props> = (props) => {
    function closeModal() {
        props.handleClick();
    }

    return (
        <div className="modal">
            <div className="modal__message">
                <div className="modal__title">
                    <p>Создание Задачи</p>
                    <div onClick={closeModal}>
                        x
                    </div>
                </div>

                <Formik
                    initialValues={{ 
                        name: "",
                        description: "",
                        executor: "",
                        status: "",
                        priority: "",
                    }}
                    validateOnChange={false}
                    validateOnBlur={true}
                    onSubmit={(val) => {
                        console.log('submit');
                        closeModal();
                    }}
                    validationSchema={validationSchema}
                >
                    {({values, errors, isSubmitting}) => (
                        <Form className="form" >
                            <Input type='text' name='name' label='Название задачи' 
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    placeholder='Название' required={true} 
                                />

                            <Input type='text' name='description' label='Описание задачи' 
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    placeholder='Надо сделать ...' required={true} 
                                />
                            
                            <Input type='text' name='executor' label='Исполнитель' 
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    placeholder='Имя' required={true} 
                                />

                            <Select name='status' label="Статус задачи" required={true}
                                    arr={["в работе", "завершена", "на проверке"]} 
                                    addEmptyOption={true} 
                                    errors={errors} isSubmitting={isSubmitting}
                                />

                            <Select name='priority' label="Приоритет задачи" required={true}
                                    arr={["высокий", "средний", "низкий"]} 
                                    addEmptyOption={true} 
                                    errors={errors} isSubmitting={isSubmitting}
                                />

                            <div className="form__buttons">
                                <Button type="submit" text='Создать' />
                            </div> 
                        </Form>
                    )}
                </Formik>        
                
            </div>
        </div>
    )
}

export default ModalTasks;