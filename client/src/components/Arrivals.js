import React from 'react'

import * as S from './Styles'

const Arrivals = ({ arrivals }) => {
    const requested = arrivals.request_time ? 'Requested ' + arrivals.request_date + ' at ' + arrivals.request_time : null
    return (<>
        <S.SubHeader>
            {requested ? (<>{requested}<br/></>) : null}
            {arrivals.common_name}
            {arrivals.stop_letter ? (<>, {arrivals.stop_letter}</>) : null}
        </S.SubHeader>
        <S.DataWrapper>
            {arrivals.arrivals.length > 0 ? arrivals.arrivals.map((arrival, index) => {
                return (
                    <S.LineWrapper key={index}>
                        <S.DataLeft>
                            {arrival.lineName}
                        </S.DataLeft>
                        <S.DataMiddle>
                            {arrival.destinationName}
                        </S.DataMiddle>
                        <S.DataRight>
                            {arrival.expectedArrival}
                        </S.DataRight>
                    </S.LineWrapper>
                )
            }) : <S.DataMiddle>No data for that stop...</S.DataMiddle>
            }
        </S.DataWrapper>
    </>
    )
}

export default Arrivals