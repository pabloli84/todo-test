describe('API Testing tasks', () => {

    it('GET-read', function () {
        cy.request('GET', 'https://damp-eyrie-62274.herokuapp.com/tasks/1').then((response) => {
            expect(response).to.have.property('status', 200)
            expect(response.body).to.not.be.null
            expect(response.body).to.have.length(1)
        })
    })
})