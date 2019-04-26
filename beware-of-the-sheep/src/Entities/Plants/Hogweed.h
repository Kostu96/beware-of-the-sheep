#pragma once
#include "Plant.h"

namespace bots {

	/*!
		\brief
		\author	Konstanty Misiak
	*/
	class Hogweed :
		public Plant
	{
	public:
		Hogweed(World & world, const Point & position);
		virtual ~Hogweed() = default;

		void action() override;
		void collision(Entity & other) override;
	protected:
		inline std::string getSymbol() const override { return "HW"; }
		inline Kind getKind() const override { return Kind::Hogweed; }
		inline std::string getClassName() const override { return "Hogweed"; }
	private:

	};

} // namespace bots
