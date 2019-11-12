import React, { useState, useEffect } from 'react'
import Arrivals from './Arrivals'
import LoadingWheel from './LoadingWheel'
import ErrorBox from './ErrorBox'

import * as S from './Styles'

const DataRenderer = ({ url, title, message }) => {
    const [data, setData] = useState()
    const [dataLoading, setDataLoading] = useState(false)
    const [dataError, setDataError] = useState(false)
    const [errorMessage, setErrorMessage] = useState('')

    const fetchData = () => {
        setDataLoading(true)
        setDataError(false)
        fetch(url)
            .then(response => {
                if (!response.ok) {
                    response.json().then(json=>setErrorMessage(json.error))
                    throw Error(response.statusText)
                }
                return response
            })
            .then(response => response.json())
            .then(json => {
                setData(json)
                setDataLoading(false)
                setDataError(false)
                setErrorMessage('')
            })
            .catch(error => {
                setData([])
                console.log(error)
                setDataLoading(false)
                setDataError(true)
            })
    }

    useEffect(fetchData, [url])

    return (
        <>
        <S.PageHeader>
            <h3>{title}</h3>
        </S.PageHeader>
        <div>
            {dataLoading ? <LoadingWheel/> : null}
            {dataError ? <ErrorBox message={errorMessage} refresh={fetchData} /> : null}
            {data && !dataLoading ? data.map((arrivals, index) => {
                return <Arrivals key={index} arrivals={arrivals} />
            }) : null}
        </div>
        {message?<p>{message}</p>:null}
        </>
    )
}

export default DataRenderer
