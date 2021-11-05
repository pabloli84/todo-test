describe('API Testing tasks', () => {

    it('GET-read', function () {
        cy.request('GET', 'http://0.0.0.0:5001/tasks').then((response) => {
            expect(response).to.have.property('status', 200)
            expect(response.body).to.not.be.null
        })
    })
})