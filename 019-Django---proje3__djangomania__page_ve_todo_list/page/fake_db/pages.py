ABOUT_US_DETAIL = '''
<div class="row">
    <div class="col-sm-8 offset-sm-2">
        <h2>Vizyonumuz</h2>
        <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Numquam, ea eaque quam labore beatae dolorum
            consectetur maiores? Libero sed quas, cumque molestiae officia et iure, odio non illum quae eius.</p>
        <p>Quod earum voluptatibus expedita corrupti quos ab ipsam accusantium deleniti illum similique nemo placeat
            sapiente molestias iure provident sequi, explicabo incidunt ut animi nihil perferendis? Perspiciatis
            repellat illo nam dignissimos?</p>
        <p>Neque itaque ipsam illo minus ullam sed voluptas quia similique incidunt magni pariatur expedita quas,
            excepturi totam tempora facilis voluptatibus. Officia a omnis, doloribus commodi ipsam deserunt est
            inventore quos!</p>

        <hr>
        <h2>Misyonumuz</h2>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt unde explicabo minus impedit pariatur harum
            ipsam optio, error tempore sint non provident aut odit nisi fugit dolorem tenetur vel! Aliquid.</p>
        <p>Sed exercitationem ad id ea? Voluptatibus veritatis cupiditate, inventore harum velit incidunt facere dolorum
            repellendus quidem repellat sapiente! Minima quaerat iste maiores soluta suscipit porro possimus officia
            doloribus obcaecati qui?</p>
        <p>Ducimus at praesentium accusamus obcaecati dolores recusandae voluptate adipisci veniam, aut, eligendi iure
            nostrum? Voluptate deserunt adipisci eos ut totam blanditiis aspernatur autem optio facere velit! Fugit
            deserunt facilis enim.</p>
        <p>Sapiente culpa ad laborum, dolore iste quia? Magni sed voluptatibus error soluta assumenda, nesciunt quas
            laboriosam ratione minima iure similique dolore nobis rem quo velit inventore expedita, ipsum corporis
            voluptate.</p>
        <ul>
            <li>Lorem, ipsum.</li>
            <li>Reiciendis, quam.</li>
            <li>Mollitia, ullam?</li>
            <li>Tenetur, ratione.</li>
        </ul>
    </div>
</div>
'''

VISION_DETAIL = '''
<div class="row">
    <div class="col-sm-8 offset-sm-2">
        <h2>Vizyonumuz</h2>
        <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Numquam, ea eaque quam labore beatae dolorum
            consectetur maiores? Libero sed quas, cumque molestiae officia et iure, odio non illum quae eius.</p>
        <p>Quod earum voluptatibus expedita corrupti quos ab ipsam accusantium deleniti illum similique nemo placeat
            sapiente molestias iure provident sequi, explicabo incidunt ut animi nihil perferendis? Perspiciatis
            repellat illo nam dignissimos?</p>
        <p>Neque itaque ipsam illo minus ullam sed voluptas quia similique incidunt magni pariatur expedita quas,
            excepturi totam tempora facilis voluptatibus. Officia a omnis, doloribus commodi ipsam deserunt est
            inventore quos!</p>

        <hr>
        <h2>Misyonumuz</h2>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt unde explicabo minus impedit pariatur harum
            ipsam optio, error tempore sint non provident aut odit nisi fugit dolorem tenetur vel! Aliquid.</p>
        <p>Sed exercitationem ad id ea? Voluptatibus veritatis cupiditate, inventore harum velit incidunt facere dolorum
            repellendus quidem repellat sapiente! Minima quaerat iste maiores soluta suscipit porro possimus officia
            doloribus obcaecati qui?</p>
        <p>Ducimus at praesentium accusamus obcaecati dolores recusandae voluptate adipisci veniam, aut, eligendi iure
            nostrum? Voluptate deserunt adipisci eos ut totam blanditiis aspernatur autem optio facere velit! Fugit
            deserunt facilis enim.</p>
        <p>Sapiente culpa ad laborum, dolore iste quia? Magni sed voluptatibus error soluta assumenda, nesciunt quas
            laboriosam ratione minima iure similique dolore nobis rem quo velit inventore expedita, ipsum corporis
            voluptate.</p>
        <ul>
            <li>Lorem, ipsum.</li>
            <li>Reiciendis, quam.</li>
            <li>Mollitia, ullam?</li>
            <li>Tenetur, ratione.</li>
        </ul>
    </div>
</div>
'''

CONTACT_DETAIL = '''
<div class="row mb-5">
        <div class="col-sm-8 offset-sm-2">
            <h2>Adresimiz</h2>
            <address>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt non architecto quidem error velit
                    tempora quisquam aut, quo perspiciatis cupiditate!</p>
            </address>
            <hr>
            <h2 class="mt-5">Bize Ulasin</h2>
            <form class="row g-3">
                <div class="col-12">
                    <label for="inputEmail4" class="form-label">Email</label>
                    <input type="email" class="form-control" id="inputEmail4">
                </div>

                <div class="col-12">
                    <label for="bilgi" class="form-label">Bilgi</label>
                    <textarea class="form-control" id="bilgi"></textarea>
                </div>

                <div class="col-12">
                    <label for="inputCity" class="form-label">Sehir</label>
                    <input type="text" class="form-control" id="inputCity">
                </div>
                <div class="col-12">
                    <label for="inputState" class="form-label">Bize Nasil Ulastin</label>
                    <select id="inputState" class="form-select">
                        <option selected>Seciminiz...</option>
                        <option>Sosyal Medya</option>
                        <option>Google</option>
                        <option>Reklam</option>
                        <option>Referams</option>
                    </select>
                </div>
                <div class="col-12">
                    <button type="submit" class="btn btn-primary">Gonder</button>
                </div>
            </form>
        </div>
    </div>
'''

FAKE_DB_PAGES = [
    {"url": "iletisim", "detail": CONTACT_DETAIL, "title": "İletişim"},
    {"url": "hakkimizda", "detail": ABOUT_US_DETAIL, "title": "Hakkımızda"},
    {"url": "vizyonumuz", "detail": VISION_DETAIL, "title": "Vizyonumuz"},
]