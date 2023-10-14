import React, { useMemo } from "react";

import TableRow from "../tableRow/TableRow";

import "./table.scss";

import arrow from '../../icons/arrow-down.svg';

interface Props {
    titles: string[],
    data: any[],
    sorting: string[],
} 


const Table: React.FC<Props> = (props) => {
    let titles = props.titles;
    let data = props.data;
    let sorting = props.sorting;

    const [tableInfo, setTableInfo] = React.useState<any[]>(data);

    const [sortParam, setSortParam] = React.useState([sorting[0], 'down']);

    function sortTable() {
        setTableInfo(prevTable => {
            if (sortParam[1] === 'down') {
                let obj = prevTable.sort((a, b) => (a[sortParam[0]] < b[sortParam[0]] ? -1 : 1));
                return obj;
            } else {
                let obj = prevTable.sort((a, b) => (a[sortParam[0]] > b[sortParam[0]] ? -1 : 1));
                return obj;
            }
        })
        return tableInfo;
    }

    function changeTable(event:any, index: number) {
        event.target.classList.toggle('table__arrow');
        let order = event.target.classList.contains('table__arrow')? 'up' : 'down'
        setSortParam([sorting[index], order]);
    }

    const array: any[] = useMemo(() => sortTable(), [sortParam, tableInfo]);
    
    return (
        <table className="table">
            <thead>
                <tr className="table__row table__header">
                    {titles.map((item, index) => {
                        return <th key={index}>
                                    <div onClick={(event) => changeTable(event, index)}>
                                        {item} <img src={arrow} alt="" />
                                    </div>
                                </th>
                    })}
                    <th><div></div></th>
                </tr>
            </thead>

            <tbody>
                {
                    array.map((item, index) => {
                    return <TableRow data={item} key={index} />
                    })
                }
            </tbody>
        </table>
    )
}

export default Table;