import React, { useState } from "react";

import { Formik, Form } from 'formik';
import * as Yup from "yup";
import Button from "../button/Button";
import Input from "../input/Input";
import './modal.scss';


const validationSchema = Yup.object().shape({
    name: Yup.string().required("Put the name"),
    description: Yup.string().required("Put the description"),
    participants: Yup.string().required("Put participants"),
    begin: Yup.string().required("Put the begin"),
    end: Yup.string().required("Put the end"),
    status: Yup.string().required("Put the status"),
});

interface Props {
    handleClick: Function,
    data: any,
}

const ModalProjectInfo: React.FC<Props> = (props) => {
    function closeModal() {
        props.handleClick();
    }
    
    const [data, setData] = useState(props.data);

    return (
        <div className="modal">
            <div className="modal__message">
                <div className="modal__title">
                    <p>Редактирование Проекта</p>
                    <div onClick={closeModal}>
                        x
                    </div>
                </div>

                <Formik
                    initialValues={{ 
                        name: data.name,
                        description: data.description,
                        participants: data.participants,
                        begin: data.begin,
                        end: data.end,
                        status: data.status
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
                            <Input type='text' name='name' label='Название проекта' 
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    placeholder='Название' required={true} 
                                />

                            <Input type='text' name='description' label='Описание проекта' 
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    placeholder='Этот проект ...' required={true} 
                                />

                            <Input type='text' name='participants' label='Участники' 
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    placeholder='Вася' required={true} 
                                />

                            <Input type='text' name='end' label='Завершение' 
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    placeholder='11' required={true} 
                                />
                                
                            <Input type='text' name='status' label='Статус' 
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    placeholder='в работе' required={true} 
                                /> 
                             
                            <div className="form__buttons">
                                <Button type="submit" text='Сохранить изменения' />
                            </div> 
                        </Form>
                    )}
                </Formik>        
                
            </div>
        </div>
    )
}

export default ModalProjectInfo;