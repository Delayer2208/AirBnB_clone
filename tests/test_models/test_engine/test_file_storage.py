        FileStorage._FileStorage__objects = {}
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.save()
        models.storage.reload()
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("City." + cy.id, models.storage.all().keys())
        self.assertIn(cy, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())

    def test_unique_reload_with_arg(self):
        """Test the reload method of FileStorage with an argument."""
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_unique_reload_no_file(self):
        """Test the reload method of FileStorage with no file."""
        if os.path.isfile("file.json"):
            os.rename("file.json", "tmp")
        with self.assertRaises(FileNotFoundError):
            models.storage.reload()
        if os.path.isfile("tmp"):
            os.rename("tmp", "file.json")


if __name__ == "__main__":
    unittest.main()
